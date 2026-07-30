import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";

function getNextY(doc, fallbackY = 40) {
  return (doc.lastAutoTable?.finalY || fallbackY) + 10;
}

function formatValue(value) {
  if (value === null || value === undefined || value === "") {
    return "-";
  }

  if (typeof value === "object") {
    try {
      return JSON.stringify(value, null, 2);
    } catch {
      return String(value);
    }
  }

  return String(value);
}

function addSectionTable(doc, title, rows, startY, options = {}) {
  autoTable(doc, {
    startY,
    head: [[title, ""]],
    body: rows,
    theme: "grid",
    styles: {
      fontSize: 10,
      cellPadding: 4,
      overflow: "linebreak",
      valign: "top",
      ...options.styles,
    },
    headStyles: {
      fillColor: [37, 99, 235],
      textColor: [255, 255, 255],
      fontStyle: "bold",
      ...options.headStyles,
    },
    columnStyles: {
      0: { cellWidth: 55, fontStyle: "bold" },
      1: { cellWidth: "auto" },
      ...(options.columnStyles || {}),
    },
    margin: { left: 14, right: 14 },
    ...options,
  });
}

export function exportDecisionReport(decision) {
  if (!decision) {
    throw new Error("No decision data provided for PDF export.");
  }

  const doc = new jsPDF();

  // ===========================
  // Header
  // ===========================

  doc.setFontSize(20);
  doc.setTextColor(37, 99, 235);
  doc.text("AI Decision Laboratory", 14, 20);

  doc.setFontSize(11);
  doc.setTextColor(100);
  doc.text("Decision Intelligence Platform", 14, 28);

  doc.setDrawColor(220);
  doc.line(14, 33, 196, 33);

  let currentY = 40;

  // ===========================
  // Decision Summary
  // ===========================

  addSectionTable(
    doc,
    "Decision Summary",
    [
      ["Decision ID", formatValue(decision.decision_id)],
      ["Decision Type", formatValue(decision.decision_type)],
      ["Status", formatValue(decision.status)],
    ],
    currentY
  );
  currentY = getNextY(doc);

  // ===========================
  // Context
  // ===========================

  addSectionTable(
    doc,
    "Business Context",
    [
      ["Business Objective", formatValue(decision.context?.business_objective)],
      ["Product ID", formatValue(decision.context?.product_id)],
      ["Priority", formatValue(decision.context?.priority)],
      ["Time Horizon", formatValue(decision.context?.time_horizon)],
    ],
    currentY
  );
  currentY = getNextY(doc);

  // ===========================
  // Selected Strategy
  // ===========================

  if (decision.selected_strategy) {
    addSectionTable(
      doc,
      "Selected Strategy",
      [
        ["Strategy", formatValue(decision.selected_strategy.name)],
        [
          "Evaluation Score",
          Number(decision.selected_strategy.score || 0).toFixed(2),
        ],
        [
          "Description",
          formatValue(decision.selected_strategy.description),
        ],
      ],
      currentY
    );
    currentY = getNextY(doc);
  }

  // ===========================
  // Expected Impact
  // ===========================

  if (
    decision.selected_strategy?.expected_impact &&
    Object.keys(decision.selected_strategy.expected_impact).length > 0
  ) {
    addSectionTable(
      doc,
      "Expected Impact",
      Object.entries(decision.selected_strategy.expected_impact).map(
        ([key, value]) => [key, formatValue(value)]
      ),
      currentY,
      {
        columnStyles: {
          0: { cellWidth: 55, fontStyle: "bold" },
          1: { cellWidth: "auto" },
        },
      }
    );
    currentY = getNextY(doc);
  }

  // ===========================
  // Alternative Strategies
  // ===========================

  if (Array.isArray(decision.strategies) && decision.strategies.length > 0) {
    addSectionTable(
      doc,
      "Alternative Strategies",
      decision.strategies.map((strategy) => [
        formatValue(strategy.name),
        Number(strategy.score || 0).toFixed(2),
      ]),
      currentY,
      {
        theme: "striped",
        columnStyles: {
          0: { cellWidth: 120, fontStyle: "bold" },
          1: { cellWidth: 30, halign: "center" },
        },
        headStyles: {
          fillColor: [37, 99, 235],
          textColor: [255, 255, 255],
          fontStyle: "bold",
        },
      }
    );
    currentY = getNextY(doc);
  }

  // ===========================
  // Business Data
  // ===========================

  if (decision.context?.business_data) {
    const businessDataEntries = Object.entries(decision.context.business_data);

    if (businessDataEntries.length > 0) {
      addSectionTable(
        doc,
        "Business Data",
        businessDataEntries.map(([key, value]) => [key, formatValue(value)]),
        currentY,
        {
          theme: "striped",
          columnStyles: {
            0: { cellWidth: 55, fontStyle: "bold" },
            1: { cellWidth: "auto" },
          },
          headStyles: {
            fillColor: [37, 99, 235],
            textColor: [255, 255, 255],
            fontStyle: "bold",
          },
        }
      );
      currentY = getNextY(doc);
    }
  }

  // ===========================
  // Footer
  // ===========================

  const pageHeight = doc.internal.pageSize.getHeight();

  doc.setFontSize(10);
  doc.setTextColor(120);
  doc.text("Generated by AI Decision Laboratory", 14, pageHeight - 10);

  doc.save(`Decision_${decision.decision_id}.pdf`);
}