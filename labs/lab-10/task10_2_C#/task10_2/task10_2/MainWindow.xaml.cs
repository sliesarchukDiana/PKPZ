using Microsoft.Win32;
using System.Data;
using System.IO;
using System.Text;
using System.Windows;

namespace GraphMatrices
{
    public partial class MainWindow
    {
        private List<(string From, string To)> edges = new();
        private List<string> vertices = new();

        public MainWindow()
        {
            InitializeComponent();
            TxtEdges.Text = "a->b; b->a; c->a; c->e; d->e; b->d;";
        }

        private void BtnClear_Click(object sender, RoutedEventArgs e)
        {
            TxtEdges.Clear();
            edges.Clear();
            vertices.Clear();
            TxtVertices.Clear();
            TxtEdgesParsed.Clear();
            GridAdj.ItemsSource = null;
            GridInc.ItemsSource = null;
        }

        private void BtnParse_Click(object sender, RoutedEventArgs e)
        {
            ParseInput(TxtEdges.Text);
            BuildAndShowMatrices();
        }

        private void ParseInput(string input)
        {
            edges.Clear();
            vertices.Clear();
            if (string.IsNullOrWhiteSpace(input)) return;
            
            var parts = input.Split(new[] { ';', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries);

            foreach (var p in parts)
            {
                var s = p.Trim();
                if (string.IsNullOrEmpty(s)) continue;
                
                var arrow = s.Split(new[] { "->" }, StringSplitOptions.None);
                if (arrow.Length != 2) continue;

                var from = arrow[0].Trim();
                var to = arrow[1].Trim();
                if (string.IsNullOrEmpty(from) || string.IsNullOrEmpty(to)) continue;

                edges.Add((from, to));
            }
            
            vertices = edges.SelectMany(e => new[] { e.From, e.To })
                            .Distinct(StringComparer.OrdinalIgnoreCase)
                            .Select(v => v.Trim())
                            .OrderBy(v => v, StringComparer.OrdinalIgnoreCase)
                            .ToList();
            TxtVertices.Text = string.Join(", ", vertices);
            TxtEdgesParsed.Text = string.Join(Environment.NewLine, edges.Select((e, i) => $"{i + 1}: {e.From} -> {e.To}"));
        }

        private void BuildAndShowMatrices()
        {
            if (vertices.Count == 0)
            {
                MessageBox.Show("No vertices parsed. Provide edges in format a->b; b->c; ...", "Info", MessageBoxButton.OK, MessageBoxImage.Information);
                return;
            }

            var adj = BuildAdjacencyMatrix();
            var inc = BuildIncidenceMatrix();

            GridAdj.ItemsSource = adj.DefaultView;
            GridInc.ItemsSource = inc.DefaultView;
        }

        private DataTable BuildAdjacencyMatrix()
        {
            var dt = new DataTable();
            
            dt.Columns.Add("Vertex", typeof(string));
            
            foreach (var v in vertices)
                dt.Columns.Add(v, typeof(int));
            
            var idx = vertices.Select((v, i) => (v, i)).ToDictionary(t => t.v, t => t.i, StringComparer.OrdinalIgnoreCase);

            // init adjacency 0
            int n = vertices.Count;
            int[,] A = new int[n, n];

            foreach (var e in edges)
            {
                if (!idx.ContainsKey(e.From) || !idx.ContainsKey(e.To)) continue;
                int i = idx[e.From];
                int j = idx[e.To];
                A[i, j] = 1;
            }
            
            for (int i = 0; i < n; i++)
            {
                var row = dt.NewRow();
                row["Vertex"] = vertices[i];
                for (int j = 0; j < n; j++)
                    row[vertices[j]] = A[i, j];
                dt.Rows.Add(row);
            }

            return dt;
        }

        private DataTable BuildIncidenceMatrix()
        {
            var dt = new DataTable();

            dt.Columns.Add("Vertex", typeof(string));
            
            for (int k = 0; k < edges.Count; k++)
            {
                var head = $"e{k + 1}: {edges[k].From}->{edges[k].To}";
                dt.Columns.Add(head, typeof(int));
            }
            
            int n = vertices.Count;
            int m = edges.Count;
            int[,] Inc = new int[n, m];

            var idx = vertices.Select((v, i) => (v, i)).ToDictionary(t => t.v, t => t.i, StringComparer.OrdinalIgnoreCase);

            for (int k = 0; k < m; k++)
            {
                var (from, to) = edges[k];
                if (!idx.ContainsKey(from) || !idx.ContainsKey(to)) continue;
                int iFrom = idx[from];
                int iTo = idx[to];
                Inc[iFrom, k] = -1;
                Inc[iTo, k] = +1;
            }
            
            for (int i = 0; i < n; i++)
            {
                var row = dt.NewRow();
                row["Vertex"] = vertices[i];
                for (int k = 0; k < m; k++)
                    row[dt.Columns[k + 1].ColumnName] = Inc[i, k];
                dt.Rows.Add(row);
            }

            return dt;
        }

        #region Save CSV
        private void BtnSaveAdj_Click(object sender, RoutedEventArgs e)
        {
            var dt = BuildAdjacencyMatrix();
            SaveDataTableToCsv(dt, "adjacency.csv");
        }

        private void BtnSaveInc_Click(object sender, RoutedEventArgs e)
        {
            var dt = BuildIncidenceMatrix();
            SaveDataTableToCsv(dt, "incidence.csv");
        }

        private void BtnSaveBoth_Click(object sender, RoutedEventArgs e)
        {
            var dlg = new SaveFileDialog { Filter = "CSV file (*.csv)|*.csv", FileName = "graph_matrices.csv" };
            if (dlg.ShowDialog() != true) return;

            using var sw = new StreamWriter(dlg.FileName, false, Encoding.UTF8);
            var adj = BuildAdjacencyMatrix();
            WriteDataTableCsv(sw, adj);
            sw.WriteLine();
            var inc = BuildIncidenceMatrix();
            WriteDataTableCsv(sw, inc);
            MessageBox.Show("Saved.", "Saved", MessageBoxButton.OK, MessageBoxImage.Information);
        }

        private void SaveDataTableToCsv(DataTable dt, string defaultName)
        {
            var dlg = new SaveFileDialog { Filter = "CSV file (*.csv)|*.csv", FileName = defaultName };
            if (dlg.ShowDialog() != true) return;
            using var sw = new StreamWriter(dlg.FileName, false, Encoding.UTF8);
            WriteDataTableCsv(sw, dt);
            MessageBox.Show("Saved.", "Saved", MessageBoxButton.OK, MessageBoxImage.Information);
        }

        private void WriteDataTableCsv(StreamWriter sw, DataTable dt)
        {
            var headers = dt.Columns.Cast<DataColumn>().Select(c => EscapeCsv(c.ColumnName));
            sw.WriteLine(string.Join(",", headers));
            foreach (DataRow r in dt.Rows)
            {
                var fields = dt.Columns.Cast<DataColumn>().Select(c => EscapeCsv(Convert.ToString(r[c])));
                sw.WriteLine(string.Join(",", fields));
            }
        }

        private string EscapeCsv(string s)
        {
            if (s is null) return "";
            if (s.Contains(",") || s.Contains("\"") || s.Contains("\n") || s.Contains("\r"))
                return "\"" + s.Replace("\"", "\"\"") + "\"";
            return s;
        }
        #endregion
    }
}
