const Lancamentos = require('../models/Lancamentos');

exports.createLancamento = async function (req, res) {
  const { id_usuario } = req.headers;
  const { id_banco, data_lancamento, descricao, categoria, valor } = req.body;

  if (!id_usuario) {
    return res.status(400).json({ error: 'Usuário não informado' });
  }

  if (!id_banco) {
    return res.status(400).json({ error: 'Banco não informado' });
  }

  if (!data_lancamento) {
    return res.status(400).json({ error: 'Data de lançamento não informada' });
  }

  if (!descricao) {
    return res.status(400).json({ error: 'Descrição não informada' });
  }

  if (!categoria) {
    return res.status(400).json({ error: 'Categoria não informada' });
  }

  if (!valor) {
    return res.status(400).json({ error: 'Valor não informado' });
  }

  const ultimoLancamento = await Lancamentos.findOne({id_banco},{}, { sort: { '_id': -1 } })
  console.log('ultimo', ultimoLancamento  )

  let saldo = 0;
  saldo = ultimoLancamento && ultimoLancamento.saldo + valor || valor;

  let Lancamento = new Lancamentos({
    id_usuario,
    id_banco,
    data_lancamento,
    descricao,
    categoria,
    valor,
    saldo
  });

  Lancamento.save((err) => {
    if (err) return res.json(err);
    return res.json('Lançamento criado com sucesso!');
  });
}