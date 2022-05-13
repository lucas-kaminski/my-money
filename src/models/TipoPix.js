const mongoose = require("mongoose");

const tipoPixSchema = new mongoose.Schema({
  tipoChave: {type: String, required: true},
});

module.exports = mongoose.model("TipoPix", tipoPixSchema)