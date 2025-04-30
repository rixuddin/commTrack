<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sales Commission Tracker</title>
    <style>
        :root {
            --primary: #4361ee;
            --secondary: #3f37c9;
            --accent: #4895ef;
            --light: #f8f9fa;
            --dark: #212529;
            --success: #4cc9f0;
            --warning: #f72585;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--dark);
            background-color: #f5f7fa;
            margin: 0;
            padding: 20px;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        
        h1, h2, h3 {
            color: var(--primary);
        }
        
        .progress-container {
            background: #e9ecef;
            border-radius: 10px;
            margin: 20px 0;
            height: 30px;
        }
        
        .progress-bar {
            background: var(--accent);
            height: 100%;
            border-radius: 10px;
            transition: width 0.5s ease;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            padding-right: 10px;
            color: white;
            font-weight: bold;
            min-width: 30px;
        }
        
        .card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            border-left: 4px solid var(--accent);
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        
        .stat-box {
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary);
            margin: 10px 0;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        
        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        th {
            background-color: var(--primary);
            color: white;
        }
        
        tr:hover {
            background-color: #f5f5f5;
        }
        
        button, input[type="submit"] {
            background: var(--primary);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            transition: background 0.3s;
        }
        
        button:hover {
            background: var(--secondary);
        }
        
        input, select {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            width: 100%;
            margin-bottom: 10px;
        }
        
        .form-group {
            margin-bottom: 15px;
        }
        
        .alert {
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }
        
        .alert-warning {
            background: #fff3cd;
            color: #856404;
            border-left: 4px solid #ffeeba;
        }
        
        .alert-success {
            background: #d4edda;
            color: #155724;
            border-left: 4px solid #c3e6cb;
        }
        
        @media (max-width: 768px) {
            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Sales Commission Tracker</h1>
        <p>Track your CTN, warranty, and residential sales to maximize earnings</p>
        
        <div class="card">
            <h2>Monthly Progress</h2>
            
            <div class="stats-grid">
                <div class="stat-box">
                    <h3>CTN (Term)</h3>
                    <div class="stat-value" id="ctn-term-count">0</div>
                    <div class="progress-container">
                        <div class="progress-bar" id="ctn-term-progress" style="width: 0%">0%</div>
                    </div>
                    <p><span id="ctn-term-remaining">100</span> remaining to goal</p>
                </div>
                
                <div class="stat-box">
                    <h3>CTN (BYOD)</h3>
                    <div class="stat-value" id="ctn-byod-count">0</div>
                </div>
                
                <div class="stat-box">
                    <h3>Warranties</h3>
                    <div class="stat-value" id="warranty-count">0</div>
                    <div class="progress-container">
                        <div class="progress-bar" id="warranty-progress" style="width: 0%">0%</div>
                    </div>
                    <p><span id="warranty-remaining">37</span> remaining to goal</p>
                </div>
                
                <div class="stat-box">
                    <h3>Residential</h3>
                    <div class="stat-value" id="residential-count">0</div>
                </div>
            </div>
            
            <div class="stats-grid">
                <div class="stat-box">
                    <h3>Projected Commission</h3>
                    <div class="stat-value">$<span id="projected-commission">0</span></div>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h2>Add Today's Sales</h2>
            <form id="sales-form">
                <div class="form-group">
                    <label for="sale-date">Date</label>
                    <input type="date" id="sale-date" required>
                </div>
                
                <div class="form-group">
                    <label for="ctn-term">CTN (Term) Activations</label>
                    <input type="number" id="ctn-term" min="0" value="0">
                </div>
                
                <div class="form-group">
                    <label for="ctn-byod">CTN (BYOD) Activations</label>
                    <input type="number" id="ctn-byod" min="0" value="0">
                </div>
                
                <div class="form-group">
                    <label for="warranties">Warranties Sold</label>
                    <input type="number" id="warranties" min="0" value="0">
                </div>
                
                <div class="form-group">
                    <label for="residential">Residential Sales</label>
                    <input type="number" id="residential" min="0" value="0">
                </div>
                
                <button type="submit">Add Sales</button>
            </form>
        </div>
        
        <div class="card">
            <h2>Sales History</h2>
            <table id="sales-table">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>CTN (Term)</th>
                        <th>CTN (BYOD)</th>
                        <th>Warranties</th>
                        <th>Residential</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="sales-data">
                    <!-- Sales data will appear here -->
                </tbody>
            </table>
        </div>
        
        <div class="card">
            <h2>Commission Breakdown</h2>
            <div id="commission-alerts"></div>
            
            <table>
                <thead>
                    <tr>
                        <th>Category</th>
                        <th>Count</th>
                        <th>Rate</th>
                        <th>Earnings</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>CTN (Term)</td>
                        <td id="commission-ctn-term">0</td>
                        <td>$40</td>
                        <td>$<span id="earnings-ctn-term">0</span></td>
                    </tr>
                    <tr>
                        <td>CTN (BYOD)</td>
                        <td id="commission-ctn-byod">0</td>
                        <td>$30</td>
                        <td>$<span id="earnings-ctn-byod">0</span></td>
                    </tr>
                    <tr>
                        <td>Warranties</td>
                        <td id="commission-warranties">0</td>
                        <td>$5</td>
                        <td>$<span id="earnings-warranties">0</span></td>
                    </tr>
                    <tr>
                        <td>Residential</td>
                        <td id="commission-residential">0</td>
                        <td>$35</td>
                        <td>$<span id="earnings-residential">0</span></td>
                    </tr>
                    <tr style="font-weight: bold; background-color: #f8f9fa;">
                        <td>Total</td>
                        <td>-</td>
                        <td>-</td>
                        <td>$<span id="earnings-total">0</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <script>
        // Store sales data in localStorage
        let salesData = JSON.parse(localStorage.getItem('salesData')) || [];
        
        // DOM Elements
        const salesForm = document.getElementById('sales-form');
        const salesTable = document.getElementById('sales-data');
        const ctnTermCount = document.getElementById('ctn-term-count');
        const ctnTermProgress = document.getElementById('ctn-term-progress');
        const ctnTermRemaining = document.getElementById('ctn-term-remaining');
        const ctnByodCount = document.getElementById('ctn-byod-count');
        const warrantyCount = document.getElementById('warranty-count');
        const warrantyProgress = document.getElementById('warranty-progress');
        const warrantyRemaining = document.getElementById('warranty-remaining');
        const residentialCount = document.getElementById('residential-count');
        const projectedCommission = document.getElementById('projected-commission');
        const commissionAlerts = document.getElementById('commission-alerts');
        
        // Commission DOM elements
        const commissionCtnTerm = document.getElementById('commission-ctn-term');
        const earningsCtnTerm = document.getElementById('earnings-ctn-term');
        const commissionCtnByod = document.getElementById('commission-ctn-byod');
        const earningsCtnByod = document.getElementById('earnings-ctn-byod');
        const commissionWarranties = document.getElementById('commission-warranties');
        const earningsWarranties = document.getElementById('earnings-warranties');
        const commissionResidential = document.getElementById('commission-residential');
        const earningsResidential = document.getElementById('earnings-residential');
        const earningsTotal = document.getElementById('earnings-total');
        
        // Constants
        const CTN_TERM_GOAL = 100;
        const WARRANTY_GOAL = 37;
        const CTN_TERM_RATE = 40;
        const CTN_BYOD_RATE = 30;
        const WARRANTY_RATE = 5;
        const RESIDENTIAL_RATE = 35;
        
        // Initialize the app
        function initApp() {
            renderSalesTable();
            updateStats();
            updateCommission();
            
            // Set default date to today
            document.getElementById('sale-date').valueAsDate = new Date();
        }
        
        // Render sales table
        function renderSalesTable() {
            salesTable.innerHTML = '';
            
            if (salesData.length === 0) {
                salesTable.innerHTML = '<tr><td colspan="6" style="text-align: center;">No sales data yet</td></tr>';
                return;
            }
            
            salesData.forEach((sale, index) => {
                const row = document.createElement('tr');
                
                row.innerHTML = `
                    <td>${formatDate(sale.date)}</td>
                    <td>${sale.ctnTerm}</td>
                    <td>${sale.ctnByod}</td>
                    <td>${sale.warranties}</td>
                    <td>${sale.residential}</td>
                    <td><button onclick="deleteSale(${index})">Delete</button></td>
                `;
                
                salesTable.appendChild(row);
            });
        }
        
        // Update statistics
        function updateStats() {
            const totals = calculateTotals();
            
            // Update counts
            ctnTermCount.textContent = totals.ctnTerm;
            ctnByodCount.textContent = totals.ctnByod;
            warrantyCount.textContent = totals.warranties;
            residentialCount.textContent = totals.residential;
            
            // Update progress bars
            const ctnTermPercent = Math.min(100, (totals.ctnTerm / CTN_TERM_GOAL) * 100);
            const warrantyPercent = Math.min(100, (totals.warranties / WARRANTY_GOAL) * 100);
            
            ctnTermProgress.style.width = `${ctnTermPercent}%`;
            ctnTermProgress.textContent = `${Math.round(ctnTermPercent)}%`;
            
            warrantyProgress.style.width = `${warrantyPercent}%`;
            warrantyProgress.textContent = `${Math.round(warrantyPercent)}%`;
            
            // Update remaining
            ctnTermRemaining.textContent = Math.max(0, CTN_TERM_GOAL - totals.ctnTerm);
            warrantyRemaining.textContent = Math.max(0, WARRANTY_GOAL - totals.warranties);
            
            // Update projected commission
            const commission = (totals.ctnTerm * CTN_TERM_RATE) + 
                             (totals.ctnByod * CTN_BYOD_RATE) + 
                             (totals.warranties * WARRANTY_RATE) + 
                             (totals.residential * RESIDENTIAL_RATE);
            
            projectedCommission.textContent = commission.toLocaleString();
        }
        
        // Update commission breakdown
        function updateCommission() {
            const totals = calculateTotals();
            
            commissionCtnTerm.textContent = totals.ctnTerm;
            earningsCtnTerm.textContent = (totals.ctnTerm * CTN_TERM_RATE).toLocaleString();
            
            commissionCtnByod.textContent = totals.ctnByod;
            earningsCtnByod.textContent = (totals.ctnByod * CTN_BYOD_RATE).toLocaleString();
            
            commissionWarranties.textContent = totals.warranties;
            earningsWarranties.textContent = (totals.warranties * WARRANTY_RATE).toLocaleString();
            
            commissionResidential.textContent = totals.residential;
            earningsResidential.textContent = (totals.residential * RESIDENTIAL_RATE).toLocaleString();
            
            const totalCommission = (totals.ctnTerm * CTN_TERM_RATE) + 
                                  (totals.ctnByod * CTN_BYOD_RATE) + 
                                  (totals.warranties * WARRANTY_RATE) + 
                                  (totals.residential * RESIDENTIAL_RATE);
            
            earningsTotal.textContent = totalCommission.toLocaleString();
            
            // Generate alerts
            generateAlerts(totals);
        }
        
        // Generate alerts based on progress
        function generateAlerts(totals) {
            commissionAlerts.innerHTML = '';
            
            if (totals.ctnTerm < CTN_TERM_GOAL) {
                const needed = CTN_TERM_GOAL - totals.ctnTerm;
                const daysLeft = daysInMonth() - new Date().getDate();
                const dailyGoal = Math.ceil(needed / Math.max(1, daysLeft));
                
                const alert = document.createElement('div');
                alert.className = 'alert alert-warning';
                alert.innerHTML = `
                    <strong>CTN (Term) Goal:</strong> You need ${needed} more Term activations to reach 100. 
                    Aim for ${dailyGoal} per day to hit your target.
                `;
                commissionAlerts.appendChild(alert);
            } else {
                const alert = document.createElement('div');
                alert.className = 'alert alert-success';
                alert.innerHTML = `
                    <strong>🎉 CTN (Term) Goal Achieved!</strong> You've hit 100+ Term activations this month.
                `;
                commissionAlerts.appendChild(alert);
            }
            
            if (totals.warranties < WARRANTY_GOAL) {
                const needed = WARRANTY_GOAL - totals.warranties;
                const daysLeft = daysInMonth() - new Date().getDate();
                const dailyGoal = Math.ceil(needed / Math.max(1, daysLeft));
                
                const alert = document.createElement('div');
                alert.className = 'alert alert-warning';
                alert.innerHTML = `
                    <strong>Warranty Goal:</strong> You need ${needed} more warranties to reach 37. 
                    Aim for ${dailyGoal} per day to maintain Plateau 4.
                `;
                commissionAlerts.appendChild(alert);
            }
        }
        
        // Calculate totals from sales data
        function calculateTotals() {
            return salesData.reduce((acc, sale) => {
                acc.ctnTerm += parseInt(sale.ctnTerm) || 0;
                acc.ctnByod += parseInt(sale.ctnByod) || 0;
                acc.warranties += parseInt(sale.warranties) || 0;
                acc.residential += parseInt(sale.residential) || 0;
                return acc;
            }, { ctnTerm: 0, ctnByod: 0, warranties: 0, residential: 0 });
        }
        
        // Add new sale
        salesForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const newSale = {
                date: document.getElementById('sale-date').value,
                ctnTerm: parseInt(document.getElementById('ctn-term').value) || 0,
                ctnByod: parseInt(document.getElementById('ctn-byod').value) || 0,
                warranties: parseInt(document.getElementById('warranties').value) || 0,
                residential: parseInt(document.getElementById('residential').value) || 0
            };
            
            salesData.push(newSale);
            localStorage.setItem('salesData', JSON.stringify(salesData));
            
            // Reset form
            document.getElementById('ctn-term').value = 0;
            document.getElementById('ctn-byod').value = 0;
            document.getElementById('warranties').value = 0;
            document.getElementById('residential').value = 0;
            
            // Update UI
            renderSalesTable();
            updateStats();
            updateCommission();
        });
        
        // Delete sale
        function deleteSale(index) {
            if (confirm('Are you sure you want to delete this sale?')) {
                salesData.splice(index, 1);
                localStorage.setItem('salesData', JSON.stringify(salesData));
                renderSalesTable();
                updateStats();
                updateCommission();
            }
        }
        
        // Helper functions
        function formatDate(dateString) {
            const options = { year: 'numeric', month: 'short', day: 'numeric' };
            return new Date(dateString).toLocaleDateString(undefined, options);
        }
        
        function daysInMonth() {
            const now = new Date();
            return new Date(now.getFullYear(), now.getMonth() + 1, 0).getDate();
        }
        
        // Initialize the app
        initApp();
    </script>
</body>
</html>
