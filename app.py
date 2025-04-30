<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Commission Tracker</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .progress-bar { height: 20px; background: #ddd; border-radius: 10px; margin: 10px 0; }
        .progress { height: 100%; background: #4CAF50; border-radius: 10px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    </style>
</head>
<body>
    <h1>Sales Commission Tracker</h1>
    
    <div>
        <h2>Monthly Goals</h2>
        <p>CTN (Term): <span id="ctnTermCount">0</span>/100</p>
        <div class="progress-bar"><div class="progress" id="ctnTermProgress"></div></div>
        
        <p>Warranties: <span id="warrantyCount">0</span>/37</p>
        <div class="progress-bar"><div class="progress" id="warrantyProgress"></div></div>
    </div>

    <h2>Add Daily Sales</h2>
    <form id="salesForm">
        <label>Date: <input type="date" id="saleDate" required></label><br>
        <label>CTN (Term): <input type="number" id="ctnTerm" min="0" value="0"></label><br>
        <label>CTN (BYOD): <input type="number" id="ctnByod" min="0" value="0"></label><br>
        <label>Warranties: <input type="number" id="warranties" min="0" value="0"></label><br>
        <label>Residential: <input type="number" id="residential" min="0" value="0"></label><br>
        <button type="submit">Save</button>
    </form>

    <h2>Sales History</h2>
    <table id="salesTable">
        <thead>
            <tr>
                <th>Date</th>
                <th>CTN (Term)</th>
                <th>CTN (BYOD)</th>
                <th>Warranties</th>
                <th>Residential</th>
            </tr>
        </thead>
        <tbody id="salesData">
            <!-- Data will appear here -->
        </tbody>
    </table>

    <script>
        // Initialize data
        let salesData = JSON.parse(localStorage.getItem('salesData')) || [];
        
        // Load today's date
        document.getElementById('saleDate').valueAsDate = new Date();
        
        // Form submission
        document.getElementById('salesForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const newSale = {
                date: document.getElementById('saleDate').value,
                ctnTerm: parseInt(document.getElementById('ctnTerm').value) || 0,
                ctnByod: parseInt(document.getElementById('ctnByod').value) || 0,
                warranties: parseInt(document.getElementById('warranties').value) || 0,
                residential: parseInt(document.getElementById('residential').value) || 0
            };
            
            salesData.push(newSale);
            localStorage.setItem('salesData', JSON.stringify(salesData));
            updateDisplay();
            
            // Reset form
            document.getElementById('ctnTerm').value = 0;
            document.getElementById('ctnByod').value = 0;
            document.getElementById('warranties').value = 0;
            document.getElementById('residential').value = 0;
        });
        
        // Update the display
        function updateDisplay() {
            const totals = salesData.reduce((acc, sale) => {
                acc.ctnTerm += sale.ctnTerm;
                acc.ctnByod += sale.ctnByod;
                acc.warranties += sale.warranties;
                acc.residential += sale.residential;
                return acc;
            }, { ctnTerm: 0, ctnByod: 0, warranties: 0, residential: 0 });
            
            // Update counts
            document.getElementById('ctnTermCount').textContent = totals.ctnTerm;
            document.getElementById('warrantyCount').textContent = totals.warranties;
            
            // Update progress bars
            document.getElementById('ctnTermProgress').style.width = `${Math.min(100, (totals.ctnTerm / 100) * 100)}%`;
            document.getElementById('warrantyProgress').style.width = `${Math.min(100, (totals.warranties / 37) * 100)}%`;
            
            // Update table
            const tableBody = document.getElementById('salesData');
            tableBody.innerHTML = '';
            salesData.forEach(sale => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${sale.date}</td>
                    <td>${sale.ctnTerm}</td>
                    <td>${sale.ctnByod}</td>
                    <td>${sale.warranties}</td>
                    <td>${sale.residential}</td>
                `;
                tableBody.appendChild(row);
            });
        }
        
        // Initial display update
        updateDisplay();
    </script>
</body>
</html>
