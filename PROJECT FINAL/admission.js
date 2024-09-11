const mongoose = require('mongoose');

mongoose.connect("mongodb://localhost:27017/college", { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB Successfully .......'))
    .catch((err) => console.log(err));

const admissionSchema = new mongoose.Schema({
    FirstName: {
        type: String,
        required: true,
        lowercase: true,
        minilength: 3,
        maxlength: 15,
        trim: true
    },
    LastName: {
        type: String,
        required: true,
        lowercase: true,
        minilength: 3,
        maxlength: 25,
        trim: true
    },
    MotherName: {
        type: String,
        required: true,
        lowercase: true,
        minilength: 6,
        maxlength: 30,
        trim: true
    },
    FatherName: {
        type: String,
        required: true,
        lowercase: true,
        minilength: 6,
        maxlength: 30,
        trim: true
    },
    Address: {
        type: String,
        required: true,
        lowercase: true,
        maxlength: 100,
        trim: true
    },
    Gender: {
        type: String,
        required: true,

    },
    Pincode: {
        type: String,
        required: true,
        maxlength: 6
    },
    Number:{
        type: String,
        required: true,
        maxlength: 10
    },
    Email:{
        type: String,
        maxlength: 50
    }    
})
const Admission = new mongoose.model("Admission", admissionSchema);
const insertDocuments = async () => {
    try {
        const first = new Admission(
            {
                FirstName: "Sayan",
                LastName: "Banerjee",
                MotherName: "Supriya Banerjee",
                FatherName: "Ankur Banerjee",
                Address: "Berhampore",
                Gender:"male",
                Pincode: "764467",
                Number: "4567889900",
                Email: "hfh7892@localStorage.com"

            });
        const result = await first.save();
        console.log(result);
    }
    catch (err) {
        console.log(err);
    }
}
insertDocuments();


