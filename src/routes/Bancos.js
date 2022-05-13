var express = require('express')
router = express.Router()

const BancosController = require('../controllers/Bancos')

router.post('/', BancosController.createBanco)
router.get('/', BancosController.getBancos)

module.exports = router