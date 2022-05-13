var express = require('express')
router = express.Router()

const ChavePixController = require('../controllers/ChavesPix')

router.post('/', ChavePixController.createChavePix)

module.exports = router