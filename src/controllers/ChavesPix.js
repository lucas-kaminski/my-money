const ChavesPix = require('../models/ChavesPix');

exports.createChavePix = async function (req, res) {
  const { tipoPix, chave } = req.body;
  const { id_usuario } = req.headers;

  if (!id_usuario) {
    return res.status(400).json({ error: 'Usuário não informado' });
  }

  if (!tipoPix || !chave) {
    return res.json('TipoPix ou chave faltando!');
  }

  let ChavePix = new ChavesPix({
    tipoPix,
    id_usuario,
    chave
  });

  ChavePix.save((err) => {
    if (err) return res.json(err);
    return res.json('Chave Pix criada com sucesso!');
  });
}