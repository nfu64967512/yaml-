import bpy
import yaml  # 導入YAML庫

# 設定動畫範圍
start_frame = bpy.context.scene.frame_start  # 獲取動畫的開始幀
end_frame = bpy.context.scene.frame_end      # 獲取動畫的結束幀

# 準備數據結構
animation_data = []

# 遍歷每一幀並提取位置信息和旋轉信息
for frame in range(start_frame, end_frame + 1):  # 循環遍歷從開始幀到結束幀的每一幀
    bpy.context.scene.frame_set(frame)  # 設置當前幀為循環中的幀
    obj = bpy.context.object  # 獲取當前選中的對象
    if obj is None:  # 如果沒有選中的對象，跳過當前幀
        print(f"No object selected at frame {frame}")
        continue
    location = obj.location  # 獲取對象的位置
    rotation = obj.rotation_euler  # 獲取對象的旋轉（以歐拉角表示）
    
    # 添加數據到列表中
    animation_data.append({
        'frame': frame,
        'position': {'x': location.x, 'y': location.y, 'z': location.z},
        'rotation': {'x': rotation.x, 'y': rotation.y, 'z': rotation.z}
    })


    

# 將數據寫入YAML文件
output_file = 'C:/Users/User/Documents/animation/animation_data.yaml'
with open(output_file, 'w') as file:
    yaml.dump({'animation_data': animation_data}, file)

print(f"Animation data successfully exported to {output_file}")
