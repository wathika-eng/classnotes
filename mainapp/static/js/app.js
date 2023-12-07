   document.addEventListener('DOMContentLoaded', function() {
    const myAlert = document.getElementById('myAlert');

  setTimeout(function() {
    myAlert.classList.remove('show');
    myAlert.classList.add('fade');
  }, 5000);

  const closeAlertBtn = document.getElementById('closeAlert');
  closeAlertBtn.addEventListener('click', function() {
    myAlert.style.display = 'none';
  });
});
