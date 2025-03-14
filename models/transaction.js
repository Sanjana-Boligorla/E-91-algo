module.exports = (sequelize, DataTypes) => {
  const Transaction = sequelize.define("Transaction", {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true
    },
    userid: {
      type: DataTypes.INTEGER,
      allowNull: false,
      field:'userid' // ✅ Force lowercase
    },
    amount: {
      type: DataTypes.FLOAT,
      allowNull: false
    },
    type: {
      type: DataTypes.STRING,
      allowNull: false
    },
    status: {
      type: DataTypes.STRING,
      allowNull: false
    },
    createdat: { 
      type: DataTypes.DATE,
      allowNull: false,
      defaultValue: sequelize.literal("CURRENT_TIMESTAMP"), 
      field:' createdat' // ✅ Force lowercase
    },
    updatedat: { 
      type: DataTypes.DATE,
      allowNull: false,
      defaultValue: sequelize.literal("CURRENT_TIMESTAMP"),
      field: 'updatedat' // ✅ Force lowercase
    }
  }, {
    timestamps: true, // Sequelize will automatically use createdAt and updatedAt
    tableName: 'Transactions'
  });

  return Transaction;
};
