var express = require('express'),
router = express.Router();

const UserController = require('../controllers/Users')

router.post('/', UserController.createUser)
router.get('/', UserController.GetAllUsers)

module.exports = router