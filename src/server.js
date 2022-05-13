require('dotenv').config()

const mongoose = require('mongoose');

const express = require('express');
const api = express()

var routes = require('./routes/index');

mongoose.connect(process.env.MONGO_URL, function(err) {
  if (err) throw err;
});

mongoose.connection.on('connected', function () {
  console.log('Mongoose default connection open');
});

// If the connection throws an error
mongoose.connection.on('error',function (err) {
  console.log('Mongoose default connection error: ' + err);
});

// When the connection is disconnected
mongoose.connection.on('disconnected', function () {
  console.log('Mongoose default connection disconnected');
});

api.use(express.json());

api.use('/', routes);

api.listen(process.env.PORT, err => {
if (err) {
  console.log(err);
  process.exit(1);
} else {
  console.log('Server started')
}
});

module.exports = api;