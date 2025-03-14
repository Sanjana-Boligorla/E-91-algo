require("dotenv").config();
const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const { Sequelize } = require("sequelize");
const { Transaction } = require("./models"); // Ensure correct model import

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.post("/api/transactions", async (req, res) => {
    try {
        const { userid, amount, type } = req.body;
        
        if (!userid || !amount || !type) {
            return res.status(400).json({ error: "Missing required fields" });
        }

        const transaction = await Transaction.create({ userid, amount, type, status: "pending" });

        res.json(transaction);
    } catch (error) {
        console.error("Transaction Error:", error);
        res.status(500).json({ error: "Transaction failed", details: error.message });
    }
});

app.get("/api/transactions/:userid", async (req, res) => {
    try {
        const transactions = await Transaction.findAll({ where: { userid: req.params.userid } });
        res.json(transactions);
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch transactions", details: error.message });
    }
});

const PORT = process.env.PORT || 5000;
app.listen(5000, () => console.log("Server running on port", 5000));
