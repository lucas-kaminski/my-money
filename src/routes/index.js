var express = require('express'),
router = express.Router();

const rUsers = require('./Users')

router.get('/', (_, res) => {
  res.json({ping: 'pong'})
})

router.use('/users', rUsers)

module.exports = router