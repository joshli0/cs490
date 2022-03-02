from .dbconn import query, commit
from .questions import does_question_exist

def get_test_ids():
	results = query("select ID from CS490Proj.Tests")
	return [ r[0] for r in results ]

def get_test_names():
	return query("select ID, Name from CS490Proj.Tests", as_dict = True)

def get_test_id(name):
	results = query("select ID from CS490Proj.Tests where Name = %s", (name, ))
	
	if results is not None and len(results) == 1:
		return results[0][0]

def does_test_exist(name):
	return get_test_id(name) is not None

def create_test(name):
	if does_test_exist(name):
		return None
	
	query("insert into CS490Proj.Tests(Name) values (%s)", (name, ))
	commit()
	
	return get_test_id(name)

def does_test_contain_question(test_id, question_id):
	results = query("select ID from CS490Proj.Tests where ID = %s and QuestionsInOrder @> array(values (%s))", (test_id, question_id))
	return len(results) == 1

def add_question(test_id, question_id, point_value):
	if does_test_contain_question(test_id, question_id):
		return False
	
	if not does_question_exist(question_id):
		return False
	
	query("update CS490Proj.Tests set QuestionsInOrder = array_append(QuestionsInOrder, %s), QuestionPoints = array_append(QuestionPoints, %s) where ID = %s", (question_id, point_value, test_id))
	commit()
	
	return True

def remove_question(test_id, question_id):
	if not does_test_contain_question(test_id, question_id):
		return False
	
	query("update CS490Proj.Tests set QuestionsInOrder = array_remove(QuestionsInOrder, %s), QuestionPoints = array_remove(QuestionPoints, QuestionPoints[array_position(QuestionsInOrder, %s)]) where ID = %s", (question_id, question_id, test_id))
	commit()
	
	return True

def get_questions_and_points(name_or_id):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	results = query("select QuestionsInOrder, QuestionPoints from CS490Proj.Tests where ID = %s", (name_or_id, ))
	
	if len(results) == 1:
		return results[0]

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

def get_user_id(username):
	response = query("select ID from CS490Proj.Users where Username = %s", (username, ))
	return response[0][0]

def submit_test_response(name_or_id, username, responses):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	query("insert into CS490Proj.TestResponses values (%s, %s, %s, False, null, null, null, null, null, False)", (name_or_id, get_user_id(username), responses))
	commit()

def set_test_comments(name_or_id, student_name, comments_on_questions, comments_on_whole_test):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	query("update CS490Proj.TestResponses set InstructorComments = %s, CommentsOnWholeTest = %s where WhichTest = %s and WhichStudent = %s", (comments_on_questions, comments_on_whole_test, name_or_id, get_user_id(student_name)))
	commit()

def set_test_manual_grades(name_or_id, student_name, manual_grades):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	query("update CS490Proj.TestResponses set InstructorGrades = %s where WhichTest = %s and WhichStudent = %s", (manual_grades, name_or_id, get_user_id(student_name)))
	commit()

def set_test_grades_released(name_or_id, student_name, released):
	if isinstance(name_or_id, str):
		name_or_id = get_test_id(name_or_id)
	
	query("update CS490Proj.TestResponses set ResultsReleased = %s where WhichTest = %s and WhichStudent = %s", (released, name_or_id, get_user_id(student_name)))
	commit()