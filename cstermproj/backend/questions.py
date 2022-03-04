from .dbconn import query, commit

def get_difficulties():
	results = query("select * from CS490Proj.Difficulties")
	return [ r[0] for r in results ]

def add_difficulty(name):
	query("insert into CS490Proj.Difficulties values (%s)", (name, ))
	commit()

def delete_difficulty(name):
	query("delete from CS490Proj.Difficulties where Name = %s", (name, ))
	commit()

def rename_difficulty(old_name, new_name):
	query("update CS490Proj.Difficulties set Name = %s where Name = %s", (new_name, old_name))
	commit()

def can_delete_difficulty(name):
	questions = query("select ID from CS490Proj.QuestionBank where Difficulty = %s", (name, ))
	return len(questions) == 0

def get_categories():
	results = query("select * from CS490Proj.QuestionCategories")
	return [ r[0] for r in results ]

def add_category(name):
	query("insert into CS490Proj.QuestionCategories values (%s)", (name, ))
	commit()

def delete_category(name):
	query("delete from CS490Proj.QuestionCategories where Name = %s", (name, ))
	commit()

def can_delete_category(name):
	questions = query("select ID from CS490Proj.QuestionBank where Category = %s", (name, ))
	return len(questions) == 0

def rename_category(old_name, new_name):
	query("update CS490Proj.QuestionCategories set Name = %s where Name = %s", (new_name, old_name))
	commit()

def get_question_ids():
	results = query("select ID from CS490Proj.QuestionBank")
	return [ r[0] for r in results ]

def does_question_exist(id):
	return id in get_question_ids()

def get_question_titles():
	return query("select ID, Title from CS490Proj.QuestionBank", as_dict = True)

def get_question(id):
	results = query("select * from CS490Proj.QuestionBank where ID = %s", (id, ), as_dict = True)
	
	if results is not None and len(results) == 1:
		return results[0]

def get_all_questions():
	return query("select * from CS490Proj.QuestionBank", as_dict = True)

def create_question(title, description, difficulty, category, function_name, test_case_args, test_case_results):
	query("insert into CS490Proj.QuestionBank(Title, Description, Difficulty, Category, FunctionName, TestCaseArgs, TestCaseOutputs) values (%s, %s, %s, %s, %s, %s, %s)", (title, description, difficulty, category, function_name, test_case_args, test_case_results))
	commit()

def edit_question(id, title, description, difficulty, category, function_name, test_case_args, test_case_results):
	query("update CS490Proj.QuestionBank set Title = %s, Description = %s, Difficulty = %s, Category = %s, FunctionName = %s, TestCaseArgs = %s, TestCaseOutputs = %s where ID = %s", (title, description, difficulty, category, function_name, test_case_args, test_case_results, id))
	commit()

def get_question_function_name(id):
	result = query("select FunctionName from CS490Proj.QuestionBank where ID = %s", (id, ))
	
	if len(result) == 1:
		return result[0][0]

def get_question_test_cases(id):
	result = query("select TestCaseArgs::text[], TestCaseOutputs::text[] from CS490Proj.QuestionBank where ID = %s", (id, ))
	
	if len(result) == 1:
		return result[0]

def delete_question(id):
	query("delete from CS490Proj.QuestionBank where ID = %s", (id, ))
	commit()

def can_delete_question(id):
	tests = query("select ID from CS490Proj.Tests where QuestionsInOrder @> array(values (%s))", (id, ))
	return len(tests) == 0