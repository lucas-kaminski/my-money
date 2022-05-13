var express = require('express'),
router = express.Router();

const rUsers = require('./Users')
const rBancos = require('./Bancos')
const rChavesPix = require('./ChavesPix')


router.get('/', (_, res) => {
  res.json({ping: 'pong'})
})

router.use('/users', rUsers)
router.use('/bancos', rBancos)
router.use('/pix', rChavesPix)

module.exports = router