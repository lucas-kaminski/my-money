const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const chavesPixSchema = new Schema({
  tipoPix: {type: Schema.Types.ObjectId, ref: 'TipoPix'},
  id_usuario: {type: Schema.Types.ObjectId, ref: 'Users'},
  chave: {type: String, required: true}
})

module.exports = mongoose.model("ChavesPix", chavesPixSchema)