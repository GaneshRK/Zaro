window.addEventListener('scroll', function(){
  var nav = document.getElementById('mainNav');
  if(window.scrollY > 50) nav.classList.add('bg-colored');
  else nav.classList.remove('bg-colored');
});
