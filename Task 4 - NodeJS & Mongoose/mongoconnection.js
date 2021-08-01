const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/DataScience', {useNewUrlParser: true, useUnifiedTopology: true});

module.exports = mongoose