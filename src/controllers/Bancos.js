const Bancos = require('../models/Bancos')

exports.createBanco = async function (req, res) {
  const { nome, agencia, contaCorrente, observacao } = req.body
  const { id_usuario } = req.headers

  if (!id_usuario) {
    return res.status(400).json({ error: 'Usuário não informado' })
  }

  if (!nome || !agencia || !contaCorrente || !observacao) {
    return res.json('Nome, agencia, conta corrente ou observação faltando!')
  }

  let Banco = new Bancos({
    id_usuario,
    nome,
    agencia,
    contaCorrente,
    observacao
  })

  Banco.save((err) => {
    if (err) return res.json(err)
    return res.json('Banco criado com sucesso!')
  })
}

exports.getBancos = async function (req, res) {
  const { id_usuario } = req.headers

  if (!id_usuario) {
    return res.status(400).json({ error: 'Usuário não informado' })
  }

  Bancos.find({ id_usuario }, (err, bancos) => {
    if (err) return res.json(err)
    return res.json(bancos)
  })
}