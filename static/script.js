// Add Test Case ---------------------------------------------------------------
element.addEventListener("click", addTestCase);
function addTestCase() {
  let div = document.createElement("div");
  let html = `
  <div class="testcase">
    <h4><label for="test_case_args">Input:</label></h4>
    <input type="text" name="test_case_args" required></br>
    <h4><label for="test_case_results">Output:</label></h4>
    <input type="text" name="test_case_results" required></br>
  </div>
  </br>
  `;
  div.innerHTML = html;
  let element = document.getElementById("testCases");
  element.appendChild(div);
}

// Add to Exam ---------------------------------------------------------------
element.addEventListener("click", addToExam);
function addToExam() {
  let div = document.createElement("div");
  let html = `
  DISPLAY QUESTION
  `;
  div.innerHTML = html;
  let element = document.getElementById("examQuestions");
  element.appendChild(div);
}

// Apply Filter ----------------------------------------------------------------
element.addEventListener("click", applyFilter);
function applyFilter() {
  // to be completed if needed
}

// Get Question Bank -----------------------------------------------------------
element.addEventListener("click", getQuestionBank);
function getQuestionBank() {
  let div = document.createElement("div");
  let html = `
  QUESTION BANK HERE
  `;
  div.innerHTML = html;
  let element = document.getElementById("displayQuestionBank");
  element.appendChild(div);
}
/* add to HTML to call
  <div id="displayQuestionBank">
   <script>
    getQuestionBank();
   </script>
  </div>
*/

// Autograde Exam  ----------------------------------------------------------------
element.addEventListener("click", autogradeExam);
function autogradeExam() {
  // to be completed if needed
}
