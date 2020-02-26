const mongoose = require('mongoose');

const LogsSchema= mongoose.Schema(
    {
        month:{
            type: String,
            required: true
        },
        day:{
            type: String,
            required: true
        },
        time:{
            type: String,
            required: true
        },
        pop_name:{
            type: String,
            required: true
        },
        source: String,
        mac: String,
        protocal: String,
        source_ip: String,
        source_ip_port: String,
        NAT_ip: String,
        NAT_ip_port: String,
        destination_ip: String,
        destination_ip_port: String   }
);
module.exports = mongoose.model('ArchLog',LogsSchema,'archLog');