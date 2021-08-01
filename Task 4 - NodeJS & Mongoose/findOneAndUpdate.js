const db = require('./mongoconnection');

const updateData = db.connection

const filter = { month_date: '1850-01' } 
const updateValue = { $set: { month_date: '1850-01', anomaly_value: -0.7, upper_95_ci: -0.757, lower_95_ci: -0.627 }} 


updateData.collection('globalClimate').findOneAndUpdate(filter, updateValue).then((result)=>{
    console.log(result)
    updateData.close()

}).catch((err)=>{
    console.log(err)
    updateData.close()
})