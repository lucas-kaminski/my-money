require('dotenv').config()

const Categorias = require('../models/Categorias')
const mongoose = require("mongoose")

const categorias = [
  new Categorias({
    descricao: 'Alimentação',
  }),
  new Categorias({
    descricao: 'Educação',
  }),
  new Categorias({
    descricao: 'Lazer',
  }),
  new Categorias({
    descricao: 'Saúde',
  }),
  new Categorias({
    descricao: 'Transporte',
  })
]

mongoose.connect(process.env.MONGO_URL).catch(err => {
  console.log(err)
  process.exit(1)
}).then(() => {
  Categorias.insertMany(categorias).then(() => {
    console.log('Categorias criadas com sucesso!')
    mongoose.connection.close()
  }).catch(err => {
    console.log(err)
    process.exit(1)
  })
})