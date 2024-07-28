document.addEventListener("DOMContentLoaded", function () {
  const resetButton = document.getElementById("reset-button");
  const number1Input = document.querySelector('input[name="var_1"]');
  const number2Input = document.querySelector('input[name="var_2"]');
  const operationSelect = document.querySelector('select[name="operation"]');
  const resultInput = document.querySelector('input[name="result"]');

  resetButton.addEventListener("click", function (event) {
    event.preventDefault(); // Prevent the form from actually submitting

    // Clear input fields
    number1Input.value = "";
    number2Input.value = "";
    operationSelect.selectedIndex = 0; // Reset the dropdown to the first option
    resultInput.value = ""; // Clear the result field
  });
});
