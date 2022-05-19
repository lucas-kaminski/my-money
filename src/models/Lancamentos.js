const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const lancamentosSchema = new Schema({
  id_usuario: {type: Schema.Types.ObjectId, ref: 'Users'},
  id_banco: {type: Schema.Types.ObjectId, ref: 'Bancos'},
  data_lancamento: {type: Date, required: true},
  descricao: {type: String, required: true},
  categoria: {type: Schema.Types.ObjectId, ref: 'Categorias'},
  valor: {type: Number, required: true},
  saldo: {type: Number, required: true}
})

module.exports = mongoose.model("Lancamentos", lancamentosSchema)