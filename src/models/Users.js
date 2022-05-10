const mongoose = require('mongoose');
const Schema = mongoose.Schema;

let UsersSchema = new Schema({
    login: {type: String, required: true, max: 100},
    password: {type: String, required: true},
});

module.exports = mongoose.model('Users', UsersSchema);