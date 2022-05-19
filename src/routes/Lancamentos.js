var express = require('express')
router = express.Router()

const LancamentosController = require('../controllers/Lancamentos')

router.post('/', LancamentosController.createLancamento)

module.exports = router