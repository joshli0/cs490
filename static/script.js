// Add Test Case ---------------------------------------------------------------
function addTestCase(id) {
  let div = document.createElement("div");
  let html = `
  <div class="testcase">
    <h4><label for="test_case_args_ID">Input:</label></h4>
    <input type="text" name="test_case_args_ID" required></br>
    <h4><label for="test_case_results_ID">Output:</label></h4>
    <input type="text" name="test_case_results_ID" required></br>
  </div>
  </br>
  `;
  div.innerHTML = html.replaceAll('ID', ''+id);
  div.id = "testcaseholder-" + id;
  let element = document.getElementById("testCases");
  element.appendChild(div);
}


prevcount = 2;
function adddefaulttestcases() {
  addTestCase(1);
  addTestCase(2);
}

function testcasecountchanged() {
  count = parseInt(document.getElementById("testcasecount").value);
  if (count > prevcount) {
    for (i=prevcount+1; i<=count; i++){
      addTestCase(i);
    }
  }
  if (count < prevcount) {
    for (i=prevcount; i>count; i--) {
      deletetestcase(i);
    }
  }
  prevcount = count;
}

function deletetestcase(id) {
  elem = document.getElementById("testcaseholder-" + id);
  elem.parentNode.removeChild(elem);
}

// Add to Exam ----------------------------------------------------------------- delete?
function addToExam() {
  let div = document.createElement("div");
  let html = `
  DISPLAY QUESTION
  `;
  div.innerHTML = html;
  let element = document.getElementById("examQuestions");
  element.appendChild(div);
}

// displayQuestionArea ---------------------------------------------------------
function displayQuestionArea() {
  let div = document.createElement("div");
  let html = `<h3><label for="exam_questions">Questions:</label></h3>`
  div.innerHTML = html;
  let element = document.getElementById("questionArea");
  element.appendChild(div);
}

// Apply Filter ----------------------------------------------------------------
function applyFilter() {
  // to be completed if needed
}

function updateQuestionPoints(qnum, shouldUpdateTotal) {
  let total = 0;
  let casenum = 0;
  while(true){
    let elem = document.getElementById("override-" + qnum + "-" + casenum)
    if(elem==null){
      break;
    }
    total += parseFloat(elem.value);
    casenum += 1;
  }
  document.getElementById("total-" + qnum).innerHTML = total;
  if(shouldUpdateTotal){
    updateTotal();
  }
}


function setUpPoints(numquestions) {
  for(i=0; i<numquestions; i++){
    updateQuestionPoints(i, false);
  }
  updateTotal();
}

function updateTotal(){
  let qnum = 0;
  let total = 0;
  while(true){
    let elem = document.getElementById("total-" + qnum);
    if(elem==null){
      break;
    }
    total += parseFloat(elem.innerHTML);
    qnum += 1;
  }
  document.getElementById("overridePoints").innerHTML = total;
}
