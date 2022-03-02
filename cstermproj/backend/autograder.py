from .tests import *
from .questions import *

def run_auto_grader_on_everything():
	for test_id, student_id in get_all_responses():
		run_auto_grader(test_id, student_id)

def run_auto_grader(test_name_or_id, student_name_or_id):
	auto_grader_grades = []
	test_case_outputs  = []
	
	responses = get_test_responses(test_name_or_id, student_name_or_id)
	questions_and_points = get_questions_and_points(test_name_or_id)
	num_questions = len(questions_and_points)
	
	for i in range(num_questions):
		question_id = questions_and_points[i][0]
		num_points  = questions_and_points[i][1]
		response    = responses[i]
		
		grades, outputs = grade_question(question_id, num_points, response)
		
		auto_grader_grades.append(grade)
		test_case_output.append(outputs)
	
	set_test_case_outputs(test_name_or_id, student_name_or_id, test_case_outputs)
	set_test_auto_grades(test_name_or_id, student_name_or_id, auto_grader_grades)

def grade_question(question_id, num_points, response):
	function_name = get_question_function_name(question_id)
	args, outputs = get_question_test_cases(question_id)
	real_outputs = []
	
	num_test_cases = len(args)
	total_things_receiving_points = float(num_test_cases * 2 + 1)
	points_for_correct_name = round(num_points / total_things_receiving_points, 2)
	points_for_correct_case = 2 * points_for_correct_name
	grades = [ points_for_correct_name ] + ([ points_for_correct_case ] * num_test_cases)
	
	# check function name
	# check each test case
	
	return grades, real_outputs