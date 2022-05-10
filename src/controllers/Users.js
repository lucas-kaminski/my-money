const Users = require('../models/Users')

exports.createUser = function (req, res) {
  let User = new Users({
    login: 'teste',
    password: 'kkk'
  })
  User.save((err) => {
    if (err) throw err
    else console.log('saved')
  })
  res.json('Criado')
}

exports.GetAllUsers = async function (req, res) {
  const users = await Users.find({});
  res.json(users)
}