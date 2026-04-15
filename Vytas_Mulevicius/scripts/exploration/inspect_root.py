import uproot
import awkward as ak

file_path = "data/00041834_00013937_1.dimuon.dst"

try:
    with uproot.open(file_path) as file:
        event_tree = file['Event;1']
        
        # Look into the Dimuon particles specific branch
        dimuon_branch_name = '_Event_Dimuon_pPhys_Particles.'
        
        if dimuon_branch_name in event_tree:
            print(f"\n--- Exploring {dimuon_branch_name} ---")
            branch = event_tree[dimuon_branch_name]
            print(f"Branch typename: {branch.typename}")
            print(f"Branch interpretation: {branch.interpretation}")
            
            # Let's see the nested structure
            print("\nSub-branches:")
            for sub_branch in branch.keys():
                 print(f"  - {sub_branch}")
                 
            # Try to read the first few events of the payload
            print("\nTrying to read the payload...")
            try:
                # payload is usually where the data is in Gaudi RootObjectRefs
                payload = event_tree[dimuon_branch_name + '/_Event_Dimuon_pPhys_Particles.payload_'].array(entry_stop=5)
                print(payload.type)
                print(payload)
            except Exception as e:
                print(f"Could not read payload directly: {e}")
                
        else:
             print(f"Branch {dimuon_branch_name} not found.")
            
except Exception as e:
    print(f"Error: {e}")
