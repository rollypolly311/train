Sub HighlightOutOfRange()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim lastCol As Long
    Dim i As Long, j As Long
    Dim lowLimit As Double
    Dim highLimit As Double

    ' Set the worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1") ' Change "Sheet1" to your actual sheet name

    ' Find the last used row and column
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    lastCol = ws.Cells(4, ws.Columns.Count).End(xlToLeft).Column

    ' Loop through each cell in rows after row 5
    For i = 6 To lastRow
        For j = 1 To lastCol
            ' Get the low and high limits from rows 4 and 5
            lowLimit = ws.Cells(4, j).Value
            highLimit = ws.Cells(5, j).Value

            ' Check if the cell value is outside the range
            If ws.Cells(i, j).Value < lowLimit Or ws.Cells(i, j).Value > highLimit Then
                ws.Cells(i, j).Interior.Color = RGB(255, 0, 0) ' Highlight cell in red
            Else
                ws.Cells(i, j).Interior.Color = xlNone ' Remove the highlight if within range
            End If
        Next j
    Next i
End Sub