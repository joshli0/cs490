from .tests import *
from .questions import *

import re

function_name_re = re.compile("def ([a-zA-Z0-9_]+)\(")

def run_auto_grader_on_everything():
	for test_id, student_id in get_all_responses():
		run_auto_grader(test_id, student_id)

def run_auto_grader(test_name_or_id, student_name_or_id):
	auto_grader_grades = []
	test_case_outputs  = []
	function_names     = []
	
	responses = get_test_responses(test_name_or_id, student_name_or_id)
	questions, points = get_questions_and_points(test_name_or_id)
	
	for i in range(len(questions)):
		grades, function_name_actual, outputs = grade_question(questions[i], points[i], responses[i])
		
		auto_grader_grades.append(grades)
		test_case_outputs.append(outputs)
		function_names.append(function_name_actual)
	
	set_test_case_outputs(test_name_or_id, student_name_or_id, test_case_outputs)
	set_test_auto_grades(test_name_or_id, student_name_or_id, auto_grader_grades)
	set_test_response_actual_function_name(test_name_or_id, student_name_or_id, function_names)

def grade_question(question_id, num_points, code):
	function_name = get_question_function_name(question_id)
	args, outputs = get_question_test_cases(question_id)
	real_outputs = []
	
	num_test_cases = len(args)
	total_things_receiving_points = float(num_test_cases * 2 + 1)
	points_for_correct_name = round(num_points / total_things_receiving_points, 2)
	points_for_correct_case = 2 * points_for_correct_name
	grades = [ points_for_correct_name ] + ([ points_for_correct_case ] * num_test_cases)
	
	fixed_code, function_name_actual, function_def_correct = check_function_definitions(code, function_name)
	fixed_code = remove_non_function_code(fixed_code)
	
	if not function_def_correct:
		grades[0] = 0
	
	for test_case_num in range(num_test_cases):
		output, success = run_test_case(fixed_code, function_name, args[test_case_num], outputs[test_case_num])
		
		real_outputs.append(output)
		if not success:
			grades[test_case_num + 1] = 0
	
	return grades, function_name_actual, real_outputs

def check_function_definitions(code, function_name):
	function_definition_names = function_name_re.findall(code)
	num_functions = len(function_definition_names)
	function_name_actual = function_name
	
	if num_functions > 0:
		for function_def in function_definition_names:
			if function_def == function_name:
				return code, function_name_actual, True
		
		code = function_name_re.sub("def " + function_name + "(", code)
		function_name_actual = function_def[0]
	else:
		function_name_actual = "(No functions found.)"
	
	return code, function_name_actual, False

def remove_non_function_code(code):
	lines = code.split("\n")
	lines_to_keep = [ line for line in lines if (line.startswith(" ") or line.startswith("\t") or line.startswith("def ")) ]
	return "\n".join(lines_to_keep)

def run_test_case(code, function_name, args, expected_output):
	exec_output = {}
	
	try:
		exec(
			code + """
	global exec_output
	exec_output["actual_output"] = """ + function_name + "(" + str(args) + """)
	exec_output["output_correct"] = (exec_output["actual_output"] == """ + str(expected_output) + ")",
			{ "exec_output": exec_output }
		)
	except:
		exec_output["actual_output" ] = None
		exec_output["output_correct"] = False
	
	return exec_output["actual_output"], exec_output["output_correct"]