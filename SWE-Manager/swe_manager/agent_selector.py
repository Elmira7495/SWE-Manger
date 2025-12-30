import pandas as pd

def load_agent_data():
    df = pd.read_csv("/Users/elmiraonagh/Desktop/courses/6444/project/SWE-manger/SWE-Manger/SWE-Manager/assets/agent_success_rate.csv")
    return df

def assign_agents (df):
    print("Selecting Agents for each instance...")
    agent_data = load_agent_data()
    
    # Create a list to store selected agents
    selected_agents = []

    # Iterate over each issue
    for _, row in df.iterrows():
        cluster_num = row['cluster']
        
        # Filter agent data for the same cluster
        sub_df = agent_data[agent_data['hdbscan_topic_all'] == cluster_num]
        
        if not sub_df.empty:
            # Find the agent with the highest success rate
            best_agent = sub_df.loc[sub_df['success_rate'].idxmax(), 'agent']
        else:
            best_agent = None  # or some default/fallback agent
        
        selected_agents.append(best_agent)

    # Add the selected agent to the original dataframe
    df['assigned_agent'] = selected_agents
    df.to_csv("/Users/elmiraonagh/Desktop/courses/6444/project/SWE-manger/SWE-Manger/SWE-Manager/data/assigned_agents.csv", index = False)
    print("Finished selecting agents...")
    return df