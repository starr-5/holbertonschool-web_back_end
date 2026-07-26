const express = require('express');
const fs = require('fs');

const database = process.argv[2];

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  fs.readFile(database, 'utf8', (err, data) => {
    if (err) {
      res.status(500).send('This is the list of our students\nCannot load the database');
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);

    let output = 'This is the list of our students\n';
    output += `Number of students: ${students.length}\n`;

    const fields = {};

    for (const student of students) {
      const values = student.split(',');
      const firstname = values[0];
      const field = values[3];

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstname);
    }

    Object.keys(fields).forEach((field) => {
      output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
    });

    res.type('text/plain');
    res.send(output.trimEnd());
  });
});

app.listen(1245);

module.exports = app;
