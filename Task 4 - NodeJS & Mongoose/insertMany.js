const db = require('./mongoconnection');

const insertData = db.connection

const insertValue = [
    { 
        month_date: '2021-01', 
        anomaly_value: -0.7, 
        upper_95_ci: -0.757, 
        lower_95_ci: -0.627 
    },
    { 
        month_date: '2021-02', 
        anomaly_value: -0.8, 
        upper_95_ci: -0.857, 
        lower_95_ci: -0.727 
    },
    { 
        month_date: '2021-03', 
        anomaly_value: -0.9, 
        upper_95_ci: -0.957, 
        lower_95_ci: -0.827 
    },
]


insertData.collection('globalClimate').insertMany(insertValue).then((result)=>{
    console.log(result)
    insertData.close()

}).catch((err)=>{
    console.log(err)
    insertData.close()
})