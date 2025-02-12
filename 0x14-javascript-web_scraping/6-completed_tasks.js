#!/usr/bin/node
/* This script computes the number of tasks completed by user id. */

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);
  const completedTasks = {};

  data.forEach((task) => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 0;
      }
      completedTasks[task.userId]++;
    }
  });

  console.log(completedTasks);
});
