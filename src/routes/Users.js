var express = require('express'),
router = express.Router();

const UserController = require('../controllers/Users')

router.post('/', UserController.createUser)
router.post('/auth', UserController.loginUser)

module.exports = router