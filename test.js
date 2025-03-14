const { Sequelize } = require("sequelize");
const sequelize = new Sequelize("fintech_db", "postgres", "ElayneDH123$", {
  host: "localhost",
  dialect: "postgres",
});

sequelize
  .authenticate()
  .then(() => {
    console.log("Connection has been established successfully.");
  })
 .catch((err) => {
    console.error("Unable to connect to the database:", err);
 });
