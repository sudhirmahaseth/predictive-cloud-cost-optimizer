import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import time
import random

# 1. Page Configuration
st.set_page_config(
    page_title="AWS Cost Optimizer Dashboard",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Predictive Infrastructure & Cloud Cost Optimizer")
st.subheader("Automated AWS FinOps Tool via Lambda, Boto3 & Pandas")
st.markdown("---")

# Sidebar Architecture Insights
st.sidebar.header("⚙️ Core Architecture")
st.sidebar.markdown("""
**AWS Serverless Workflow:**
- **Trigger:** CloudWatch Scheduled Event (Cron)
- **Execution:** AWS Lambda Engine
- **SDK & Logic:** Python Boto3 & Pandas
- **Goal:** Automatic scaling & cleanup of idle non-prod assets.
""")

# 2. Simulated Core Function matching user logic
def simulate_lambda_handler():
    st.markdown("### 🪵 Live Lambda Execution Logs (`lambda_handler`)")
    
    with st.status("Initializing Boto3 clients & scanning AWS topology...", expanded=True) as status:
        time.sleep(1)
        st.write(f"[INFO] Cost optimization workflow triggered at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
        
        # 1. Fetching instances
        st.write("[INFO] Querying EC2 Registry with filters: `instance-state=running`, `Environment=Development,Staging`...")
        time.sleep(1)
        
        mock_instances = [
            {"InstanceId": "i-0abcd1234ef56789a", "Name": "dev-api-gateway"},
            {"InstanceId": "i-0bcde2345fg67890b", "Name": "staging-auth-db"},
            {"InstanceId": "i-0cdef3456gh78901c", "Name": "dev-testing-worker"},
            {"InstanceId": "i-0def45678ij89012d", "Name": "nonprod-cache-redis"}
        ]
        st.write(f"[SUCCESS] Discovered {len(mock_instances)} active non-production instances for auditing.")
        
        # 2. Analyze CloudWatch CPU Metrics using Pandas
        st.write("[INFO] Extracting 4-hour time-series telemetry data from CloudWatch Metrics...")
        time.sleep(1.5)
        
        idle_instances = []
        chart_data_list = []
        
        # Generating realistic metrics for simulation to feed Pandas logic
        for inst in mock_instances:
            # Generate dummy timestamps & CPU usage
            timestamps = [datetime.utcnow() - timedelta(minutes=5*i) for i in range(48)]
            
            if "db" in inst["Name"] or "api" in inst["Name"]:
                # Active instance
                cpu_values = [random.uniform(15.0, 65.0) for _ in range(48)]
            else:
                # Idle instance (Matches predictive rule: mean < 5% and max < 10%)
                cpu_values = [random.uniform(1.2, 4.5) for _ in range(48)]
                
            # --- PANDAS LOGIC FROM YOUR ORIGINAL SCRIPT ---
            df = pd.DataFrame({'Timestamp': timestamps, 'CPU': cpu_values})
            mean_cpu = df['CPU'].mean()
            max_cpu = df['CPU'].max()
            
            st.write(f"🔍 Auditing `{inst['InstanceId']}` ({inst['Name']}) -> Pandas Metrics: Mean CPU = **{mean_cpu:.2f}%**, Max CPU = **{max_cpu:.2f}%**")
            
            # Save for plotting
            df['InstanceId'] = inst['Name']
            chart_data_list.append(df)
            
            # Predictive rule evaluation
            if mean_cpu < 5.0 and max_cpu < 10.0:
                idle_instances.append(inst['InstanceId'])
        
        time.sleep(1)
        # 3. Orchestrate cost savings via Boto3
        if idle_instances:
            st.write(f"⚠️ [WARN] Identified {len(idle_instances)} severely underutilized instances: {idle_instances}")
            st.write(f"[ACTION] Dispatching `ec2_client.stop_instances(InstanceIds={idle_instances})` API call.")
            message = f"Successfully stopped {len(idle_instances)} underutilized instances to save costs."
        else:
            message = "All running assets conform to active production scaling constraints."
            
        status.update(label="Optimization Cycle Finished!", state="complete", expanded=False)
        
    st.success(f"🏆 Lambda Result: {message}")
    
    # 4. Render Analytics & Charts
    st.markdown("---")
    st.markdown("### 📈 CloudWatch Telemetry Data Visualizer (Pandas Aggregation)")
    
    full_df = pd.concat(chart_data_list)
    fig = px.line(full_df, x='Timestamp', y='CPU', color='InstanceId', title="4-Hour Lookback Window Instance CPU Tracks")
    fig.add_hline(y=5.0, line_dash="dash", line_color="red", annotation_text="Idle Mean Threshold (5%)")
    st.plotly_chart(fig, use_container_width=True)
    
    # Financial metrics
    st.markdown("#### 💎 Estimated Monthly Savings Summary")
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="Total Billing Overhead Reduction", value="25%", delta="-\$1,450 Saved/Mo")
    with c2:
        # Mini bar chart for resource saving areas
        savings_breakdown = pd.DataFrame({
            "Resource Optimization Area": ["EC2 Computing", "EBS Volumes Saved", "Elastic IP Purging"],
            "Savings Amount (\$)": [950, 380, 120]
        })
        fig_bar = px.bar(savings_breakdown, x="Resource Optimization Area", y="Savings Amount (\$)", text_auto=True)
        st.plotly_chart(fig_bar, use_container_width=True)

# 3. Streamlit Frontend Layout
st.markdown("### 🚀 Interactive Production Simulation")
st.write("Trigger the button below to see how your backend Python script handles live metric payloads, executes Pandas telemetry parsing, and flags waste.")

if st.button("▶️ Execute Lambda Automation Run", type="primary"):
    simulate_lambda_handler()
else:
    st.info("Awaiting execution trigger to simulate cloud compute scaling rules.")
            
