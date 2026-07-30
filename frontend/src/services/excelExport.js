import ExcelJS from "exceljs";
import { saveAs } from "file-saver";

export async function exportDecisionHistory(decisions) {
  const workbook = new ExcelJS.Workbook();

  workbook.creator = "AI Decision Laboratory";
  workbook.company = "Decision Intelligence Platform";
  workbook.created = new Date();

  const worksheet = workbook.addWorksheet("Decision History");

  worksheet.columns = [
    {
      header: "Decision ID",
      key: "decision_id",
      width: 28,
    },
    {
      header: "Decision Type",
      key: "decision_type",
      width: 28,
    },
    {
      header: "Status",
      key: "status",
      width: 18,
    },
  ];

  // Header style
  worksheet.getRow(1).font = {
    bold: true,
    color: { argb: "FFFFFFFF" },
  };

  worksheet.getRow(1).fill = {
    type: "pattern",
    pattern: "solid",
    fgColor: { argb: "2563EB" },
  };

  worksheet.getRow(1).alignment = {
    horizontal: "center",
    vertical: "middle",
  };

  // Add data
  decisions.forEach((decision) => {
    worksheet.addRow({
      decision_id: decision.decision_id,
      decision_type: decision.decision_type,
      status: decision.status,
    });
  });

  // Auto center status column
  worksheet.getColumn("status").alignment = {
    horizontal: "center",
  };

  // Add borders
  worksheet.eachRow((row) => {
    row.eachCell((cell) => {
      cell.border = {
        top: { style: "thin" },
        left: { style: "thin" },
        bottom: { style: "thin" },
        right: { style: "thin" },
      };
    });
  });

  const buffer = await workbook.xlsx.writeBuffer();

  saveAs(
    new Blob([buffer]),
    "Decision_History.xlsx"
  );
}   