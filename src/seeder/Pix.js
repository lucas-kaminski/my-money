require('dotenv').config()

const TipoPix = require('../models/TipoPix')
const mongoose = require("mongoose")

const chavesPix = [
  new TipoPix({
    tipoChave: 'CPF/CNPJ',
  }),
  new TipoPix({
    tipoChave: 'e-mail',
  }),
  new TipoPix({
    tipoChave: 'Telefone',
  }),
  new TipoPix({
    tipoChave: 'Aleatória',
  })
]

mongoose.connect(process.env.MONGO_URL).catch(err => {
  console.log(err)
  process.exit(1)
}).then(() => {
  TipoPix.insertMany(chavesPix).then(() => {
    console.log('TipoPix criado com sucesso!')
    mongoose.connection.close()
  }).catch(err => {
    console.log(err)
    process.exit(1)
  })
})