const Users = require('../models/Users')

exports.createUser = function (req, res) {
  const { login, password } = req.body

  if (!login || !password) {
    return res.json('Login ou senha faltando!')
  }

  console.log(login, password)

  let User = new Users({
    login,
    password
  })

  User.save((err) => {
    if (err) throw err
  })

  return res.json('Usuário criado com sucesso!')
}

exports.loginUser = async function (req, res) {
  const {login, password} = req.body

  console.log(login, password)

  if (!login || !password) {
    return res.json('Login ou senha faltando!')
  }

  const user = await Users.findOne({ login })
  if (!user) return res.json('Usuario não encontrado')

  user.comparePassword(password, (err, isMatch) => {
    if (err) throw err
    if (isMatch) return res.json('Logado')
    else return res.json('Senha incorreta')
  })
}