'use strict';
/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable("Transactions", {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      userid: {
        type: Sequelize.INTEGER,
        field: "userid"
      },
      amount: {
        type: Sequelize.DECIMAL
      },
      type: {
        type: Sequelize.STRING
      },
      status: {
        type: Sequelize.STRING
      },
      createdat: {
        allowNull: false,
        type: Sequelize.DATE,
        field: "createdat" 
      },
      updatedat: {
        allowNull: false,
        type: Sequelize.DATE,
        field: "updatedat" 
      }
    });
  },
  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable("Transactions");
  }
};