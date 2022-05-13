const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const BancosSchema = new Schema({
  id_usuario: { type: Schema.Types.ObjectId, ref: 'Users' },
  nome: { type: String, required: true },
  agencia: { type: String, required: true },
  contaCorrente: { type: String, required: true },
  pix: { type:  Schema.Types.ObjectId, ref: 'ChavePix' },
  observacao: { type: String, required: true }
})

BancosSchema.pre('save', function (next, req) {
  var Users = mongoose.model('Users')
  Users.findById(this.id_usuario, function (err, found) {
    if (found) {
      next()
    } else {
      next('Usuário não encontrado')
    }
  })
})

module.exports = mongoose.model('Bancos', BancosSchema);
