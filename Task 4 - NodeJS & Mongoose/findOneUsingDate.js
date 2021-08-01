const db = require('./mongoconnection');

const findUsingDate = db.connection

const filter = { month_date: '1850-01' } 

findUsingDate.collection('globalClimate').findOne(filter).then((result)=> {
    console.log(result)
    findUsingDate.close();
})