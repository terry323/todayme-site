async function getResponse() {
  const userInput = document.getElementById('userInput').value;
  const responseBox = document.getElementById('responseBox');
  const res = await fetch('responses/en_responses.json');
  const data = await res.json();
  const response = data[Math.floor(Math.random() * data.length)];
  responseBox.innerText = response.text;
}