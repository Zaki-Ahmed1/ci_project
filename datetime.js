const moment = require("moment");
const runs = 1000;

function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1) + min); //The maximum is inclusive and the minimum is inclusive
}

function generateTestCase() {
  const secSinceEpoch = getRandomIntInclusive(0, 253402243200);
  const date = moment.unix(secSinceEpoch).utc();

  const month = String(date.month() + 1).padStart(2, "0");
  const day = String(date.date()).padStart(2, "0");
  const year = date.year();

  return `${secSinceEpoch} ${month}-${day}-${year}`;
}

for (let i = 0; i < runs - 1; i++) {
  console.log(generateTestCase());
}

process.stdout.write(generateTestCase());
