const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const categoriasSchema = new Schema({
  descricao: {type: String, required: true}
})

module.exports = mongoose.model("Categorias", categoriasSchema)