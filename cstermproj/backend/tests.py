from json import loads as from_json, dumps as to_json

from .dbconn import query, commit
from .login import get_user_id
from .questions import does_question_exist

def get_test_ids():
	results = query("select ID from CS490Proj.Tests")
	return [ r[0] for r in results ]

def get_test_names():
	return [ q[0] for q in query("select Name from CS490Proj.Tests") ]

def get_test_ids_and_names():
	return query("select ID, Name from CS490Proj.Tests", as_dict = True)

def get_test_id(name):
	results = query("select ID from CS490Proj.Tests where Name = %s", (name, ))
	
	if results is not None and len(results) == 1:
		return results[0][0]

def get_test_name(id):
	results = query("select Name from CS490Proj.Tests where ID = %s", (id, ))
	
	if results is not None and len(results) == 1:
		return results[0][0]

def does_test_exist(name):
	return get_test_id(name) is not None

def create_test(name):
	if does_test_exist(name):
		return None
	
	empty_json = to_json([])
	query("insert into CS490Proj.Tests(Name, QuestionsInOrder, QuestionPoints) values (%s, %s, %s)", (name, empty_json, empty_json))
	commit()
	
	return get_test_id(name)

def does_test_contain_question(test_id, question_id):
	questions, _ = get_questions_and_points(test_id)
	return questions is not None and question_id in questions

def add_question(test_id, question_id, point_value):
	if does_test_contain_question(test_id, question_id):
		return False
	
	if not does_question_exist(question_id):
		return False
	
	questions, points = get_questions_and_points(test_id)
	questions.append(question_id)
	points.append(point_value)
	
	query("update CS490Proj.Tests set QuestionsInOrder = %s, QuestionPoints = %s where ID = %s", (to_json(questions), to_json(points), test_id))
	commit()
	
	return True

def remove_question(test_id, question_id):
	if not does_test_contain_question(test_id, question_id):
		return False
	
	questions, points = get_questions_and_points(test_id)
	pos = questions.index(question_id)
	del questions[pos]
	del points[pos]
	
	query("update CS490Proj.Tests set QuestionsInOrder = %s, QuestionPoints = %s where ID = %s", (to_json(questions), to_json(points), test_id))
	commit()
	
	return True

def get_questions_and_points(name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	results = query("select QuestionsInOrder, QuestionPoints from CS490Proj.Tests where ID = %s", (name_or_id, ))
	
	if len(results) == 1:
		return from_json(results[0][0]), from_json(results[0][1])

def get_num_questions(name_or_id):
	questions, _ = get_questions_and_points(name_or_id)
	return len(questions)

def can_delete_test(name):
	if not does_test_exist(name):
		return False
	
	responses = query("select * from CS490Proj.TestResponses where WhichTest = %s", (get_test_id(name), ))
	if len(responses) > 0:
		return False
	
	return True

def delete_test(name):
	if not can_delete_test(name):
		return False
	
	query("delete from CS490Proj.Tests where Name = %s", (name, ))
	commit()
	
	return True

def delete_all_responses(name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	query("delete from CS490Proj.TestResponses where WhichTest = %s", (name_or_id, ))
	commit()

def get_user_id(username):
	response = query("select ID from CS490Proj.Users where Username = %s", (username, ))
	return response[0][0]

def get_all_responses():
	return query("select WhichTest, WhichStudent from CS490Proj.TestResponses")

def get_tests_taken_by(name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_user_id(name_or_id)
	
	response = query("select WhichTest from CS490Proj.TestResponses where WhichStudent = %s", (name_or_id, ))
	return [r[0] for r in response]

def submit_test_response(name_or_id, student_name_or_id, responses):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	query("insert into CS490Proj.TestResponses values (%s, %s, %s, False, null, null, null, null, null, null, False)", (name_or_id, student_name_or_id, responses))
	commit()

def get_test_responses(name_or_id, student_name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	results = query("select Responses::text[] from CS490Proj.TestResponses where WhichTest = %s and WhichStudent = %s", (name_or_id, student_name_or_id))
	
	if len(results) == 1:
		return results[0][0]

def set_test_comments(name_or_id, student_name_or_id, comments_on_questions, comments_on_whole_test):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	query("update CS490Proj.TestResponses set InstructorComments = %s, CommentsOnWholeTest = %s where WhichTest = %s and WhichStudent = %s", (comments_on_questions, comments_on_whole_test, name_or_id, student_name_or_id))
	commit()

def get_test_comments(name_or_id, student_name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	results = query("select InstructorComments, CommentsOnWholeTest from CS490Proj.TestResponses where WhichTest = %s and WhichStudent = %s", (name_or_id, student_name_or_id))
	
	if len(results) == 1:
		return results[0]

def set_test_manual_grades(name_or_id, student_name_or_id, manual_grades):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	query("update CS490Proj.TestResponses set InstructorGrades = %s where WhichTest = %s and WhichStudent = %s", ([to_json(grade) for grade in manual_grades], name_or_id, student_name_or_id))
	commit()

def get_test_manual_grades(name_or_id, student_name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	results = query("select InstructorGrades from CS490Proj.TestResponses where WhichTest = %s and WhichStudent = %s", (name_or_id, student_name_or_id))
	
	if len(results) == 1:
		return [from_json(res) for res in results[0][0]]

def set_test_grades_released(name_or_id, student_name_or_id, released):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	query("update CS490Proj.TestResponses set ResultsReleased = %s where WhichTest = %s and WhichStudent = %s", (released, name_or_id, student_name_or_id))
	commit()

def get_test_grades_released(name_or_id, student_name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	results = query("select ResultsReleased from CS490Proj.TestResponses where WhichTest = %s and WhichStudent = %s", (name_or_id, student_name_or_id))
	
	if len(results) == 1:
		return results[0][0]

def set_test_auto_grades(name_or_id, student_name_or_id, auto_grades):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	query("update CS490Proj.TestResponses set AutoGraderGrades = %s, AutoGraderRun = True where WhichTest = %s and WhichStudent = %s", ([to_json(grade) for grade in auto_grades], name_or_id, student_name_or_id))
	commit()

def has_auto_grader_run(name_or_id, student_name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	result = query("select AutoGraderRun from CS490Proj.TestResponses where WhichTest = %s and WhichStudent = %s", (name_or_id, student_name_or_id))
	
	if result is not None and len(result) == 1:
		return result[0][0]

def get_test_auto_grades(name_or_id, student_name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	results = query("select AutoGraderGrades from CS490Proj.TestResponses where WhichTest = %s and WhichStudent = %s", (name_or_id, student_name_or_id))
	
	if len(results) == 1:
		return [from_json(g) for g in results[0][0]]

def set_test_response_actual_function_names(name_or_id, student_name_or_id, function_name):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	query("update CS490Proj.TestResponses set FunctionNamesActual = %s where WhichTest = %s and WhichStudent = %s", (function_name, name_or_id, student_name_or_id))
	commit()

def get_test_response_actual_function_names(name_or_id, student_name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	results = query("select FunctionNamesActual from CS490Proj.TestResponses where WhichTest = %s and WhichStudent = %s", (name_or_id, student_name_or_id))
	
	if len(results) == 1:
		return results[0][0]

def set_test_case_outputs(name_or_id, student_name_or_id, test_case_outputs):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	query("update CS490Proj.TestResponses set TestCaseOutputsActual = %s where WhichTest = %s and WhichStudent = %s", ([to_json(out) for out in test_case_outputs], name_or_id, student_name_or_id))
	commit()

def get_test_case_outputs(name_or_id, student_name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	results = query("select TestCaseOutputsActual from CS490Proj.TestResponses where WhichTest = %s and WhichStudent = %s", (name_or_id, student_name_or_id))
	
	if len(results) == 1:
		return [from_json(res) for res in results[0][0]]

def set_test_response_detected_constraints(name_or_id, student_name_or_id, constraints):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	query("update CS490Proj.TestResponses set ConstraintsDetected = %s where WhichTest = %s and WhichStudent = %s", (constraints, name_or_id, student_name_or_id))
	commit()

def get_test_response_detected_constraints(name_or_id, student_name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	if isinstance(student_name_or_id, str):
		student_name_or_id = get_user_id(student_name_or_id)
	
	results = query("select ConstraintsDetected::text[] from CS490Proj.TestResponses where WhichTest = %s and WhichStudent = %s", (name_or_id, student_name_or_id))
	
	if len(results) == 1:
		return results[0][0]